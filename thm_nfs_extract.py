def clean_nfs_data(raw_file, cleaned_file):
    with open(raw_file, "rb") as f_in:
        data = f_in.read()

    zip_signature = b"\x50\x4B\x03\x04"
    start_index = data.find(zip_signature)

    if start_index == -1:
        print("Zip signature not found.")
        return

    cleaned_data = data[start_index:]

    with open(cleaned_file, "wb") as f_out:
        f_out.write(cleaned_data)

clean_nfs_data("nfs_data.raw", "hidden_stash_cleaned.zip")
