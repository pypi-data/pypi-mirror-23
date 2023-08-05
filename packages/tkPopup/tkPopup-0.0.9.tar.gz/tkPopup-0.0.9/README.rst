=========================
Tkinter extension tkPopup
=========================

The package contains 3 classes, each a pop-up window based on Tkinter.
Purpose is to simplify user-interaction.

Classes **WindowOptions** and **WindowButtons** are multiple choice pop-ups,

Class **WindowEntries** is a multiple parameter input popup

-----------------------------------------------------------------

1. class **WindowOptions**

    This class accepts a list of (sting) choices,
    creates a (tkinter) window with option buttons for each choice,
    waits for the user to select one and press the 'Continue' button
    - or Cancel
    
    Args:
       choicelist:  a list or tuple containing string descriptions of the
                   different choices.
       
    Kwargs:
       master= (tk.Frame instance): parent window frame, if any. Default is
                to create a new independent top-level window

       title= (string): Window title. Default is 'Choose'

       preset= (integer): index integer to pre-select one of the options in
                choicelist. Default is 0

    Returns: 
       <class instance>.get() returns an integer value:
           integer in range(len(choicelist)) # that is 0 ... len(choicelist)-1

               or

           *-1*    for Cancel or zero-length of choicelist
    Note:
        Calling the .get() function closes and destroys the class WindowOptions
    
    Raises:
       Don't know what surprises are there!

    Sample call:

            inst = WindowCoice(['option 1','text 2], title='Select one', preset=0)
            inst.mainloop()
            index = inst.get()

        Note: calling methode get() closes WindowOptions"""

-------------------------------------------------------------------------

2. class **WindowButtons** :
    
    This class accepts a list of (sting) choices,
    creates a (tkinter) window with one button for each choice,
    waits for the user to select one - or Cancel.
    There is no 'Accept' button; clicking on one of the choices is enough.
    
    Args:
       choicelist:  a list or tuple containing string descriptions of the
                   different choices.
       
    Kwargs:
       master= (tk.Frame instance): parent window frame, if any. Default is
                to create a new independent top-level window

       title= (string): Window title. Default is 'Choose'

    Returns: 
       <class instance>.get() returns an integer value:
           integer in range(len(choicelist)) # that is 0 ... len(choicelist)-1

               or

           -1    for Cancel or zero-length of choicelist
    Note:
        Calling the .get() function closes and destroys the class WindowButtons
    
    Raises:
       Don't know what surprises are there!

    Sample call:

            inst = WindowButtons(['option 1','text 2], title='Select one')
            inst.mainloop()
            index = inst.get()

        Note: calling methode get() closes WindowButtons

------------------------------------------------------------------------

3. class **WindowEntries**:
   
    This class accepts a list of tuples describing each (text) entry.
    Each descriptor tuple must contain 4 fields:

           1. a string containing the prompt text (i.e. what is expected)

           2. an integer defining the maximum number of characters allowed

           3. a string containing a pre-set text, if any.

           4. a string containing a comment or unit descriptor, if any

    The class creates a (tkinter) window with one line for each descriptor
    tuple, consisting of the prompt column, entry field column
    and comment/unit descriptor column.
    It waits for the user to fill out all entry columns and press the 'Ok'
    button - or Cancel button.
    
    Args:
       choicelist:  a list or tuple containing descriptor tuples of entries
                    expected. See example below.
       
    Kwargs:
       master= (tk.Frame instance): parent window frame, if any. Default is
                to create a new independent top-level window

       title= (string): Window title. Default is 'Please enter'

    Special:
            if Comment/Unit text contains 'askdirectory', then
            it will be replaced by a button calling tkFileDialog.askdirectory()

            if Comment/Unit text contains 'asksaveasfilename', then
            it will be replaced by a button calling tkFileDialog.asksaveasfilename()
            
    Returns: 
       <class instance>.get() returns a list of text entries

               or

       [None, .., None]    for Cancel or zero-length of choicelist

    Note:
        Calling the .get() function closes and destroys the class WindowEntries
    
    Raises:
       Don't know what surprises are there!

    Sample call:

            specs = (('Picture Base Directory',75, '/home/franz/',None),
                     ('Subdirectory',24, 'python','askdirectory'),
                     ('Supplier code',4,None,'Empty=all'))
            inst = WindowEntries(specs, title='Enter parameters')
            inst.mainloop()
            index = inst.get()

        Note: calling methode get() closes WindowEntries

Enjoy!
