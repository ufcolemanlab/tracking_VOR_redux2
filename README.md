# Python-tracking-code---black-mice

Code being developed by the Coleman lab for tracking mice in video files (black/dark mice on a white/light background = BW).  

We use files generated by a Raspberry Pi camera (*.h264 files).  

Use the following scripts together:  
batch_roi - Set field bounds and object to track; run first to select field corners and subject (mouse)  
batch_vet - Vet the ROIs and check for accuracy; run one final time to verify all mice are being tracked (green rectangle)
batch_get - Generates the data; run this script once tracking ROIs are validated, set and working; MAT files will be written with data
