def clean_nfs_data(raw_data, cleaned_file):
    """
    Cleans raw NFS data to extract a zip archive.

    Args:
        raw_data (bytes): The raw NFS data as bytes.
        cleaned_file (str): The path to save the cleaned zip file.
    """
    zip_signature = b"\x50\x4B\x03\x04"
    start_index = raw_data.find(zip_signature)

    if start_index == -1:
        print("Zip signature not found.")
        return

    cleaned_data = raw_data[start_index:]

    with open(cleaned_file, "wb") as f_out:
        f_out.write(cleaned_data)

if __name__ == "__main__":
    try:
        raw_file_name = input("Enter the raw data file name: ")
        cleaned_file_name = input("Enter the cleaned zip file name: ")

        with open(raw_file_name, "rb") as f_in:
            raw_data = f_in.read()

        clean_nfs_data(raw_data, cleaned_file_name)
        print(f"Cleaned data saved to {cleaned_file_name}")

    except FileNotFoundError:
        print("Error: One or more files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
