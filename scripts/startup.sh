docker run -it --mount type=bind,source="$(pwd)",dst="/code" -p 3000:3000 python bash