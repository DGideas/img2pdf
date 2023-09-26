from os import listdir
from os.path import isfile, join
from PIL import Image
from argparse import ArgumentParser

parser = ArgumentParser(
    prog="img2pdf",
    description="Convert images to pdf",
)

parser.add_argument(
    "input_directory",
    action="store",
)

parser.add_argument(
    "-o",
    "--output",
    action="store",
    required=True,
)

args: dict = vars(parser.parse_args())

input_directory: str = args["input_directory"]
output_filename: str = args["output"]

onlyfiles = sorted([f for f in listdir(input_directory) if isfile(join(input_directory, f))])

images = [Image.open(input_directory + f) for f in onlyfiles]

images[0].save(
    output_filename, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
)
