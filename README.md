this project is "speaker recognition with ui" and we used these resources as the basic code(with some changes)
https://github.com/abhijeet3922/Speaker-identification-using-GMMs
https://appliedmachinelearning.blog/2017/11/14/spoken-speaker-identification-based-on-gaussian-mixture-models-python-implementation/ 

download these files to development-set:
https://www.dropbox.com/s/87v8jxxu9tvbkns/development_set.zip?dl=0

in order to add new speaker:   
1- add user directory (with name style and structure of built-in speakers) in development-set    
2- add username.gmm to speaker-models   
3- add file names to development_set_enroll file   

recording config   
new audio files are recorded using "RecordPad Sound Recorder"   
set wave encoder options(tool button in front of output- format)    
1- sample rate 11025 HZ   
2- sample size 16 bits

code is commented!
