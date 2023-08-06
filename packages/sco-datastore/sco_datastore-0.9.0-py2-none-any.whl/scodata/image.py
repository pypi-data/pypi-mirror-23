"""Images and Image Store - Collection of methods to manage image files,
collections of images, and their properties.
"""

import datetime
import os
import shutil
import uuid

import attribute
import datastore


# ------------------------------------------------------------------------------
#
# Constants
#
# ------------------------------------------------------------------------------

PROPERTY_GROUPSIZE = 'size'

# ------------------------------------------------------------------------------
# Dictionary of valid suffixes for image files and their respective Mime types.
# ------------------------------------------------------------------------------
VALID_IMGFILE_SUFFIXES = {
    '.jpg' : 'image/jpeg',
    '.jpeg' : 'image/jpeg',
    '.png' : 'image/png',
    '.gif' : 'image/gif'}


"""Unique identifier for image resource handles."""
TYPE_IMAGE = 'IMAGE'
TYPE_IMAGE_GROUP = 'IMAGE_GROUP'
TYPE_PREDICTION_IMAGE_SET = 'PREDICTION_IMAGE_SET'


# ------------------------------------------------------------------------------
#
# Images and Image Collection Classes
#
# ------------------------------------------------------------------------------

class ImageHandle(datastore.DataObjectHandle):
    """Handle to access and manipulate an image file. Each object has an unique
    identifier, the timestamp of it's creation, a list of properties, and a
    reference to the (unique) directory where the image file is stored on disk.
    File name and Mime type of the image are part of the mandatory, immutable
    set of image properties.

    Attributes
    ----------
    image_file : string
        Absolute path to image file on local disk
    """
    def __init__(self, identifier, properties, directory, timestamp=None, is_active=True):
        """Initialize the image handle. The directory references a directory
        on the local disk that contains the image files. The original image
        file name is part of the property set.

        Parameters
        ----------
        identifier : string
            Unique object identifier
        properties : Dictionary
            Dictionary of subject specific properties
        directory : string
            Directory on local disk that contains image file
        timestamp : datetime, optional
            Time stamp of object creation (UTC).
        is_active : Boolean, optional
            Flag indicating whether the object is active or has been deleted.
        """
        # Initialize super class
        super(ImageHandle, self).__init__(
            identifier,
            timestamp,
            properties,
            directory,
            is_active=is_active
        )

    @property
    def image_file(self):
        """Reference to image data file on disk."""
        return os.path.join(self.directory, self.properties[datastore.PROPERTY_FILENAME])

    @property
    def type(self):
        """Override the type method of the base class."""
        return TYPE_IMAGE


class ImageGroupHandle(datastore.DataObjectHandle):
    """Handle to access and manipulate a collection of image files. Each
    collection has an unique identifier, the timestamp of it's creation, a
    list of properties, a reference to the directory where a zipped tar-file
    containing images in the group is stored.

    In addition to the general data object properties, image groups contain a
    list of object identifier for image objects in the collection.

    Attributes
    ----------
    images : List(string)
        List of object identifier for images in the collection
    options: Dictionary(attribute.Attribute)
        Dictionary of typed attributes defining the image group options
    """
    def __init__(self, identifier, properties, directory, images, options, timestamp=None, is_active=True):
        """Initialize the image group handle. The directory references a
        directory on the local disk that contains the tar-file with all images.
        The name of that tar-file is part of the property set.

        Parameters
        ----------
        identifier : string
            Unique object identifier
        properties : Dictionary
            Dictionary of subject specific properties
        directory : string
            Directory on local disk that contains images tar-file file
        images : List(GroupImage)
            List of images in the collection
        options: Dictionary(attribute.Attribute)
            Dictionary of typed attributes defining the image group options
        timestamp : datetime, optional
            Time stamp of object creation (UTC).
        is_active : Boolean, optional
            Flag indicating whether the object is active or has been deleted.
        """
        # Initialize super class
        super(ImageGroupHandle, self).__init__(
            identifier,
            timestamp,
            properties,
            directory,
            is_active=is_active
        )
        # Initialize local object variables
        self.images = images
        self.options = options

    @property
    def data_file(self):
        """Reference to image group archive data file on disk."""
        return os.path.join(self.directory, self.properties[datastore.PROPERTY_FILENAME])

    @property
    def type(self):
        """Override the type method of the base class."""
        return TYPE_IMAGE_GROUP


class PredictionImageSetHandle(datastore.ObjectHandle):
    """A list of images that are generated as result of a successful model run.
    For each input image to the model a set of output images is maintained.
    Images are standard image resources. The images in an output set for an
    input image are expected to be uniquely identifiable based on some
    combination of the object properties.

    Attributes
    ----------
    images : list(PredictionImageSet)
        List of image sets
    """
    def __init__(self, identifier, properties, images, timestamp=None, is_active=True):
        """Initialize the image group handle. The directory references a
        directory on the local disk that contains the tar-file with all images.
        The name of that tar-file is part of the property set.

        Parameters
        ----------
        identifier : string
            Unique object identifier
        properties : Dictionary
            Dictionary of subject specific properties
        images : list(PredictionImageSet)
            List of image sets
        timestamp : datetime, optional
            Time stamp of object creation (UTC).
        is_active : Boolean, optional
            Flag indicating whether the object is active or has been deleted.
        """
        # Initialize super class
        super(PredictionImageSetHandle, self).__init__(
            identifier,
            timestamp,
            properties,
            is_active=is_active
        )
        # Initialize local object variables
        self.images = images

    @property
    def type(self):
        """Override the type method of the base class."""
        return TYPE_PREDICTION_IMAGE_SET


class GroupImage(object):
    """Descriptor for images in an image group - Each image in an image group
    has a name and folder. Together they form a unique identifier of the image,
    just like the image identifier that is also part of the group image object.

    Attributes
    ----------
    identifier : string
        Unique identifier of the image
    folder : string
        (Sub-)folder in the grouop (default: /)
    name : string
        Image name (unique within the folder)
    """
    def __init__(self, identifier, folder, name, filename):
        """Initialize attributes of the group image.

        Parameters
        ----------
        identifier : string
            Unique identifier of the image
        folder : string
            (Sub-)folder in the group (default: /)
        name : string
            Image name (unique within the folder)
        filename : string
            Absolute path to file on local disk
        """
        self.identifier = identifier
        self.folder = folder
        self.name = name
        self.filename = filename


class PredictionImageSet(object):
    """Set of generated images for an input image in a successful model run.
    Maintains references to the input image and all of the outputs.

    Attributes
    ----------
    input_image : ImageHandle
        Handle for input image
    output_images : list(ImageHandle)
        List of output images that were generated for an input image
    """
    def __init__(self, input_image, output_images):
        """Set the resource handles for input and output images.

        Parameters
        ----------
        input_image : ImageHandle
            Handle for input image
        output_images : list(ImageHandle)
            List of output images that were generated for an input image
        """
        self.input_image = input_image
        self.output_images = output_images


# ------------------------------------------------------------------------------
#
# Object Stores
#
# ------------------------------------------------------------------------------

class DefaultImageManager(datastore.DefaultObjectStore):
    """Default Image Manager - Manager for images objects. Image objects are
    stored in folders that are named by a prefix of the object identifier.

    This is a default implentation that uses MongoDB as storage backend.

    Attributes
    ----------
    directory : string
        Base directory on local disk for image files.
    """
    def __init__(self, mongo_collection, base_directory):
        """Initialize the MongoDB collection and base directory where to store
        images files. Set immutable and mandatory properties.

        Parameters
        ----------
        mongo_collection : Collection
            Collection in MongoDB storing image information
        base_directory : string
            Base directory on local disk for image files. Files are stored
            in sub-directories named by the subject identifier. To avoid having
            too many files in a single directory we group these sub-directories
            in directories that start with the first two characters of the
            object identifier.
        """
        # Initialize the super class
        super(DefaultImageManager, self).__init__(
            mongo_collection,
            base_directory,
            [
                datastore.PROPERTY_FILENAME,
                datastore.PROPERTY_FILESIZE,
                datastore.PROPERTY_MIMETYPE
            ]
        )

    def create_object(self, filename, img_properties=None):
        """Create an image object on local disk from the given file. The file
        is copied to a new local directory that is created for the image object.
        The optional list of image properties will be associated with the new
        object together with the set of default properties for images.

        Parameters
        ----------
        filename : string
            Path to file on disk
        img_properties : Dictionary, optional
            Set of image properties.

        Returns
        -------
        ImageHandle
            Handle for created image object
        """
        # Get the file name, i.e., last component of the given absolute path
        prop_name = os.path.basename(os.path.normpath(filename))
        # Ensure that the image file has a valid suffix. Currently we do not
        # check whether the file actually is an image. If the suffix is valid
        # get the associated Mime type from the dictionary.
        prop_mime = None
        pos = prop_name.rfind('.')
        if pos >= 0:
            suffix = prop_name[pos:].lower()
            if suffix in VALID_IMGFILE_SUFFIXES:
                prop_mime = VALID_IMGFILE_SUFFIXES[suffix]
        if not prop_mime:
            raise ValueError('unsupported image type: ' + prop_name)
        # Create a new object identifier.
        identifier = str(uuid.uuid4()).replace('-','')
        # The sub-folder to store the image is given by the first two
        # characters of the identifier.
        image_dir = self.get_directory(identifier)
        # Create the directory if it doesn't exists
        if not os.access(image_dir, os.F_OK):
            os.makedirs(image_dir)
        # Create the initial set of properties for the new image object.
        properties = {
            datastore.PROPERTY_NAME: prop_name,
            datastore.PROPERTY_FILENAME : prop_name,
            datastore.PROPERTY_FILESIZE : os.path.getsize(filename),
            datastore.PROPERTY_MIMETYPE : prop_mime
        }
        # Add additional image properties (if given). Note that this will not
        # override the default image properties.
        if not img_properties is None:
            for prop in img_properties:
                if not prop in properties:
                    properties[prop] = img_properties[prop]
        # Copy original file to new object's directory
        shutil.copyfile(filename, os.path.join(image_dir, prop_name))
        # Create object handle and store it in database before returning it
        obj = ImageHandle(identifier, properties, image_dir)
        self.insert_object(obj)
        return obj

    def from_dict(self, document):
        """Create image object from JSON document retrieved from database.

        Parameters
        ----------
        document : JSON
            Json document in database

        Returns
        -------
        ImageHandle
            Handle for image object
        """
        # Get object properties from Json document
        identifier = str(document['_id'])
        active = document['active']
        timestamp = datetime.datetime.strptime(document['timestamp'], '%Y-%m-%dT%H:%M:%S.%f')
        properties = document['properties']
        # The directory is not materilaized in database to allow moving the
        # base directory without having to update the database.
        directory = self.get_directory(identifier)
        # Cretae image handle
        return ImageHandle(identifier, properties, directory, timestamp=timestamp, is_active=active)

    def get_directory(self, identifier):
        """Implements the policy for naming directories for image objects. Image
        object directories are name by their identifier. In addition, these
        directories are grouped in parent directories named by the first two
        characters of the identifier. The aim is to avoid having too many
        sub-folders in a single directory.

        Parameters
        ----------
        identifier : string
            Unique object identifier

        Returns
        -------
        string
            Path to image objects data directory
        """
        return os.path.join(
            os.path.join(self.directory, identifier[:2]),
            identifier
        )


class DefaultImageGroupManager(datastore.DefaultObjectStore):
    """Default Image Group Manager - Manager for image collections objects.

    This is a default implentation that uses MongoDB as storage backend.

    Attributes
    ----------
    attribute_defs : list(dict(...))
        List of definitions of valid image group options
    directory : string
        Base directory on local disk for image group files.
    """
    def __init__(self, mongo_collection, base_directory, image_manager, attribute_defs=None):
        """Initialize the MongoDB collection and base directory where to store
        images group files. Set immutable and mandatory properties.

        Parameters
        ----------
        mongo_collection : Collection
            Collection in MongoDB storing image group information
        base_directory : string
            Base directory on local disk for image group files. Files are stored
            in sub-directories named by the subject identifier.
        image_manager : DefaultImageManager
            Manager for image files
        attribute_defs : list(dict(...)), optional
            List of definitions of valid image group options
        """
        # Initialize the super class
        super(DefaultImageGroupManager, self).__init__(
            mongo_collection,
            base_directory,
            [
                datastore.PROPERTY_FILENAME,
                datastore.PROPERTY_FILESIZE,
                datastore.PROPERTY_MIMETYPE
            ]
        )
        # Add group size as read-only property
        self.immutable_properties.add(PROPERTY_GROUPSIZE)
        # Initialize image manager reference
        self.image_manager = image_manager
        # Set image grup option definitions. Use default definitions if given
        # argument is None
        if not attribute_defs is None:
            self.attribute_defs = attribute_defs
        else:
            self.attribute_defs = [
                attribute.AttributeDefinition(
                    'aperture_radius',
                    'aperture_radius',
                    'aperture_radius (default: None)\n\n' +
                    '(images) aperture_radius: Specifies the radius of the ' +
                    'aperture in degrees; by default this is None,\n        ' +
                    'indicating that no aperture should be used; otherwise ' +
                    'the aperture is applied after\n        ' +
                    'normalizing the images.',
                    attribute.FloatType()
                ),
                attribute.AttributeDefinition(
                    'pixels_per_degree',
                    'pixels_per_degree',
                    'pixels_per_degree\n\n(images) ' +
                    'pixels_per_degree: Must specify the number of pixels ' +
                    'per degree in the input images; note\n        ' +
                    'that all stimulus images must have the same ' +
                    'pixels_per_degree value.',
                    attribute.FloatType()
                ),
                attribute.AttributeDefinition(
                    'background',
                    'background',
                    'background (default: 0.5)\n\n(images) ' +
                    'background: Specifies the background color of the ' +
                    'stimulus; by default this is 0.5 (gray);\n        ' +
                    'this is only used if an aperture is applied.',
                    attribute.FloatType(),
                    default=0.5
                ),
                attribute.AttributeDefinition(
                    'aperture_edge_width',
                    'aperture_edge_width',
                    'aperture_edge_width (default: None)\n\n' +
                    '(images) aperture_edge_width: Specifies the width of ' +
                    'the aperture edge in degrees; by default this is\n' +
                    '        1; if 0, then no aperture edge is used.',
                    attribute.FloatType()
                ),
                attribute.AttributeDefinition(
                    'gamma',
                    'gamma',
                    'gamma (default: None)\n\n' +
                    '(gamma_correction) gamma: May be given, in which case ' +
                    'it must be one of:\n        - an (n x 2) or (2 x n) ' +
                    'matrix such that is equivalent to (potentially after ' +
                    'transposition)\n          a matrix of (x,y) values ' +
                    'where x is the input gamma and y is the corrected gamma\n'+
                    '        - a vector of corrected gamma values; if the ' +
                    'vector u is of length n, then this is \n          ' +
                    'equivalent to passing a matrix in which the y-values ' +
                    'are the elements of u and the\n          x-values are ' +
                    'evenly spaced values that cover the interval [0,1]; ' +
                    'accordingly there must be\n          at least 2 ' +
                    'elements\n        - a function that accepts a number ' +
                    'between 0 and 1 and returns the corrected gamma\n' +
                    '        By default this is None, and no gamma ' +
                    'correction is applied.',
                    attribute.ListType()
                )
            ]


    def create_object(self, name, images, filename, options=None, object_identifier=None, read_only=False):
        """Create an image group object with the given list of images. The
        file name specifies the location on local disk where the tar-file
        containing the image group files is located. The file will be copied
        to the image groups data directory.

        Parameters
        ----------
        name : string
            User-provided name for the image group
        images : List(GroupImage)
            List of objects describing images in the group
        filename : string
            Location of local file containing all images in the group
        options : list(dict('name':...,'value:...')), optional
            List of image group options. If None, default values will be used.
        object_identifier : string
            Unique object identifier, optional
        read_only : boolean, optional
            Optional value for the read-only property

        Returns
        -------
        ImageGroupHandle
            Object handle for created image group
        """
        # Raise an exception if given image group is not valied.
        self.validate_group(images)
        # Create a new object identifier if none is given.
        if object_identifier is None:
            identifier = str(uuid.uuid4()).replace('-','')
        else:
            identifier = object_identifier
        # Create the initial set of properties.
        prop_filename = os.path.basename(os.path.normpath(filename))
        prop_mime = 'application/x-tar' if filename.endswith('.tar') else 'application/x-gzip'
        properties = {
            datastore.PROPERTY_NAME: name,
            datastore.PROPERTY_FILENAME : prop_filename,
            datastore.PROPERTY_FILESIZE : os.path.getsize(filename),
            datastore.PROPERTY_MIMETYPE : prop_mime
        }
        if read_only:
            properties[datastore.PROPERTY_READONLY] = True
        # Directories are simply named by object identifier
        directory = os.path.join(self.directory, identifier)
        # Create the directory if it doesn't exists
        if not os.access(directory, os.F_OK):
            os.makedirs(directory)
        # Move original file to object directory
        shutil.copyfile(filename, os.path.join(directory, prop_filename))
        # Get dictionary of given options. If none are given opts will be an
        # empty dictionary. If duplicate attribute names are present an
        # exception will be raised.
        opts = attribute.to_dict(options, self.attribute_defs)
        # Create the image group object and store it in the database before
        # returning it.
        obj = ImageGroupHandle(
            identifier,
            properties,
            directory,
            images,
            opts
        )
        self.insert_object(obj)
        return obj

    def from_dict(self, document):
        """Create image group object from JSON document retrieved from database.

        Parameters
        ----------
        document : JSON
            Json document in database

        Returns
        -------
        ImageGroupHandle
            Handle for image group object
        """
        # Get object attributes from Json document
        identifier = str(document['_id'])
        # Create list of group images from Json
        images = list()
        for grp_image in document['images']:
            images.append(GroupImage(
                grp_image['identifier'],
                grp_image['folder'],
                grp_image['name'],
                os.path.join(
                    self.image_manager.get_directory(grp_image['identifier']),
                    grp_image['name']
                )
            ))
        # Create list of properties and add group size
        properties = document['properties']
        properties[PROPERTY_GROUPSIZE] = len(document['images'])
        # Directories are simply named by object identifier
        directory = os.path.join(self.directory, identifier)
        # Create image group handle.
        return ImageGroupHandle(
            identifier,
            properties,
            directory,
            images,
            attribute.attributes_from_dict(document['options']),
            timestamp=datetime.datetime.strptime(
                document['timestamp'],
                '%Y-%m-%dT%H:%M:%S.%f'
            ),
            is_active=document['active']
        )

    def get_collections_for_image(self, image_id):
        """Get identifier of all collections that contain a given image.

        Parameters
        ----------
        image_id : string
            Unique identifierof image object

        Returns
        -------
        List(string)
            List of image collection identifier
        """
        result = []
        # Get all active collections that contain the image identifier
        for document in self.collection.find({'active' : True, 'images.identifier' : image_id}):
            result.append(str(document['_id']))
        return result

    def list_images(self, identifier, offset=-1, limit=-1):
        """
        Parameters
        ----------
        identifier : string
            Unique image group identifier
        limit : int
            Limit number of results in returned object listing
        offset : int
            Set offset in list (order as defined by object store)

        Returns
        -------
        ObjectListing
            Listing of group images or None if image group does not exist
        """
        # Get image group to ensure that it exists. The object contains the full
        # list of group images
        img_grp = self.get_object(identifier)
        if img_grp is None:
            return None
        # Extract subset of group images based on offset and limit arguments
        total_count = len(img_grp.images)
        items = []
        if offset < total_count:
            if limit > 0:
                list_end = min((offset + limit), total_count)
            else:
                list_end = total_count
            for i in range(offset, list_end):
                items.append(img_grp.images[i])
        # Return object listing
        return datastore.ObjectListing(items, offset, limit, total_count)

    def to_dict(self, img_coll):
        """Create a Json-like dictionary for image group. Extends the basic
        object with an array of image identifiers.

        Parameters
        ----------
        img_coll : ImageGroupHandle

        Returns
        -------
        (JSON)
            Json-like object, i.e., dictionary.
        """
        # Get the basic Json object from the super class
        json_obj = super(DefaultImageGroupManager, self).to_dict(img_coll)
        # Add list of images as Json array
        images = []
        for img_group in img_coll.images:
            images.append({
                'identifier' : img_group.identifier,
                'folder' : img_group.folder,
                'name' : img_group.name
            })
        json_obj['images'] = images
        # Transform dictionary of options into list of elements, one per typed
        # attribute in the options set.
        json_obj['options'] = attribute.attributes_to_dict(img_coll.options)
        return json_obj

    def update_object_options(self, identifier, options):
        """Update set of typed attributes (options) that are associated with
        a given image group. Raises a ValueError if any of the given
        attributes violates the attribute definitions associated with image
        groups.

        Parameters
        ----------
        identifier : string
            Unique object identifier
        options : list(dict('name':...,'value:...'))
            List of attribute instances

        Returns
        -------
        ImageGroupHandle
            Handle for updated image group or None if identifier is unknown.
        """
        # Retrieve object from database to ensure that it exists
        img_group = self.get_object(identifier)
        if img_group is None:
            return None
        # Replace existing object in database with object having given options.
        # Raises an exception of attributes with duplicate names appear in the
        # list.
        img_group.options = attribute.to_dict(options, self.attribute_defs)
        self.replace_object(img_group)
        # Return image group handle
        return img_group

    @staticmethod
    def validate_group(images):
        """Validates that the combination of folder and name for all images in
        a group is unique. Raises a ValueError exception if uniqueness
        constraint is violated.

        Parameters
        ----------
        images : List(GroupImage)
            List of images in group
        """
        image_ids = set()
        for image in images:
            key = image.folder + image.name
            if key in image_ids:
                raise ValueError('Duplicate images in group: ' + key)
            else:
                image_ids.add(key)


class DefaultPredictionImageSetManager(datastore.MongoDBStore):
    """Default data store backend for prediction image sets that uses MongoDB
    as storage backend.
    """
    def __init__(self, mongo_collection, image_manager):
        """Initialize the MongoDB collection and the image manager to retrieve
        set images.

        Parameters
        ----------
        mongo_collection : Collection
            Collection in MongoDB storing image group information
        image_manager : DefaultImageManager
            Manager for image files
        """
        # Initialize the super class
        super(DefaultPredictionImageSetManager, self).__init__(mongo_collection)
        # Initialize image manager reference
        self.image_manager = image_manager


    def create_object(self, name, filename):
        """Create a prediction image set list from a given tar-file. For each
        image in the tar-file an image resource will be created.

        Parameters
        ----------
        name : string
            User-provided name for the image group.
        filename : string
            Location of local tar-file containing all images in the set

        Returns
        -------
        PredictionImageSetHandle
            Object handle for created prediction image set
        """
        pass

    def from_dict(self, document):
        """Create a prediction image set resource from a dictionary
        serialization.

        Parameters
        ----------
        document : dict
            Dictionary serialization of the resource

        Returns
        -------
        PredictionImageSetHandle
            Handle for prediction image set
        """
        pass

    def to_dict(self, img_set):
        """Create a dictionary serialization for a prediction image set.

        Parameters
        ----------
        img_set : PredictionImageSet

        Returns
        -------
        dict
            Dictionary serialization of the resource
        """
        pass


# ------------------------------------------------------------------------------
#
# Helper methods
#
# ------------------------------------------------------------------------------
def get_image_files(directory, files):
    """Recursively iterate through directory tree and list all files that have a
    valid image file suffix

    Parameters
    ----------
    directory : directory
        Path to directory on disk
    files : List(string)
        List of file names

    Returns
    -------
    List(string)
        List of files that have a valid image suffix
    """
    # For each file in the directory test if it is a valid image file or a
    # sub-directory.
    for f in os.listdir(directory):
        abs_file = os.path.join(directory, f)
        if os.path.isdir(abs_file):
            # Recursively iterate through sub-directories
            get_image_files(abs_file, files)
        else:
            # Add to file collection if has valid suffix
            if '.' in f and '.' + f.rsplit('.', 1)[1] in VALID_IMGFILE_SUFFIXES:
                files.append(abs_file)
    return files
