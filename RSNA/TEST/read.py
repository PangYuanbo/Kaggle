import pydicom

# Load the DICOM file
dicom_file_path = '4290709089_3390218084_6.dcm'
dicom_data = pydicom.dcmread(dicom_file_path)

# Extract metadata and display basic details about the DICOM file
metadata = dicom_data.dir()
metadata_summary = {tag: getattr(dicom_data, tag, 'Not available') for tag in metadata}

print(metadata_summary)
