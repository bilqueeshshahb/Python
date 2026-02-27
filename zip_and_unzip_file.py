#10.write a program to zip and unzip particular file.import zipfile
import zipfile
import os

def zip_file(file_path, zip_name):
    """Create a zip file from a single file"""
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_path, arcname=os.path.basename(file_path))
    print(f"✓ Created: {zip_name}")

def unzip_file(zip_path, extract_dir='.'):
    """Extract contents of a zip file"""
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_dir)
    print(f"✓ Extracted to: {extract_dir}")

# Example usage
if __name__ == "__main__":
    # Create a sample file to zip
    with open("sample.txt", "w") as f:
        f.write("Hello, this is a sample file!")
    
    # Zip the file
    zip_file("sample.txt", "sample.zip")
    
    # Unzip the file
    unzip_file("sample.zip", "extracted")
