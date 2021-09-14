The project has been developed using the tkinter library in Python. This library is primarily used for GUI development. Apart from this, the main libraries that have been imported are tkintker, ImageTK, Image from PILLOW, and pygame which helps access different controls within the system.  
To begin, we have created an object of the tkinter class containing the main window of the system. All of the different features an accesses are seen as well as implemented from this root object. The mainloopfunction ensures that the window runs continuously until the user presses the exit button.  
When it comes to the working of our project, the program begins with the initialization of the window. We’ve used multiple widgets, such as buttons and labels to welcome the user to MusicApp. Each button on the main screen has been given an on-action function, which performs various actions as defined in each function’s body. These actions take place whenever the respective function is called. 
Most of the variables and widgets used in the code have been declared to be global. This ensures that they  can be accessed within various functions to either be used or to be destroyed as per user commands.  
The second page of the system displays various music genres for the user to choose from, which are:  
- Study beats  
- Indian Classical  
- Electronic/Dance  
- Pop Culture  
- Anime  

The file locations have been passed into the working directory, which is then iterated through and stored in  a listbox widget from the tkinter library.  
The access controls over the song have been implemented using the play, pause, stop, and resume buttons.  These buttons are enabled using the inbuilt functions – play, pause, stop, and resume – which act on the  current process. In this case, the current process is the song playing.  
Lastly, a volume scale as well as a volume function have been defined to help the user control the volume of  the song playing on the application. The default volume when the user opens the app is initially set to 0,  but can be increased or decreased according to his/her choice.  

 
