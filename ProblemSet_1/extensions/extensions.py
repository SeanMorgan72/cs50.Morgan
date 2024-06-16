def get_media_type(filename):
    # Dictionary of known media types
    media_types = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'
    }
    
    # Extract the file extension (case insensitive)
    file_extension = filename.lower().rpartition('.')[-1]
    file_extension = '.' + file_extension if file_extension else ''
    
    # Return the media type if recognized, otherwise default to 'application/octet-stream'
    return media_types.get(file_extension, 'application/octet-stream')

def main():
    # Prompt the user for a file name
    filename = input("Enter the file name: ").strip()

    # Output the media type
    print("Media type:", get_media_type(filename))

if __name__ == "__main__":
    main()
