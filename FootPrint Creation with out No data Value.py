import os
from osgeo import gdal

# Enable exceptions
gdal.UseExceptions()

# 📂 Folders
input_folder = r"I:\Tiff"
output_folder = r"I:\Foot Print"
os.makedirs(output_folder, exist_ok=True)

raster_extensions = (".tif", ".tiff", ".jp2", ".img", ".vrt", ".png", ".jpg", ".ecw", ".sid")

file_count = 0

for filename in os.listdir(input_folder):
    if filename.lower().endswith(raster_extensions):

        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(
            output_folder,
            os.path.splitext(filename)[0] + ".shp"
        )

        print(f"📍 Creating TRUE footprint (NoData ignored): {filename}")

        try:
            # Remove old shapefile
            for ext in [".shp", ".shx", ".dbf", ".prj", ".cpg"]:
                f = output_path.replace(".shp", ext)
                if os.path.exists(f):
                    os.remove(f)

            # ✅ MINIMAL & COMPATIBLE call
            gdal.Footprint(output_path, input_path)

            print(f"✅ Footprint created: {output_path}")
            file_count += 1

        except Exception as e:
            print(f"❌ Failed: {filename}")
            print(e)

if file_count == 0:
    print("⚠️ No footprints created.")
else:
    print(f"🎉 Done! {file_count} TRUE footprints created.")
