To run this:
In VS Code run the 1.py file
after succesfully running the 1.py file, it will create runs folder, inside the runs folder, it will create detect folder, inside the detect folder it will create train folder, indie that will find the weights.pt folder, inside that best.pt, rename the best.pt to yolov8m_custom.pt
then run:  yolo task=detect mode=predict model=yolov8m_custom.pt show=True conf=0.5 source=1.jpg
it will detect the electronic components.

Since it is taking much time in CPU  for the epochs
I tried this running in the google colab
I have attached the google colab file(Run\inGoogleColab.ipynb)
please try to run in the same order
