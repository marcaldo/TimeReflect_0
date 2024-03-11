import os

class AlbumStorage:
    def get_album_names(self, folder_path):
        """
        Get a collection of directory names in the specified folder.

        Args:
        folder_path (str): The path to the folder.

        Returns:
        list: A collection of directory names in the specified folder.
        """
        directory_names = []
        # Check if the folder path exists
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            # Iterate over all entries in the folder
            for entry in os.listdir(folder_path):
                # Check if the entry is a directory
                if os.path.isdir(os.path.join(folder_path, entry)):
                    directory_names.append(entry)
        else:
            print("Error: Folder path does not exist or is not a directory.")
        return directory_names
    
    def get_file_names(self, album_path):
        file_names = []
        if os.path.exists(album_path) and os.path.isdir(album_path):
            for entry in os.listdir(album_path):
                if os.path.isfile(os.path.join(album_path, entry)):
                    file_names.append(entry)
        else:
            print("Error: Folder path does not exist or is not a directory.")
        return file_names
