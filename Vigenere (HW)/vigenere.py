## vigenere.py
##
## Name : Jake Hennessy
## Date : 3.9.2014
## Class : CSCI 220
## Prof : Stalvey
##
## Certification of authenticity :
##        I certify that this program is my own work.
##
## Purpose :
##    This program will provide the user with a graphical user interface (GUI)
##    that will accept a phrase from the user along with a keyword that will
##    either encrypt or decrypt the phrase according to the Vigenere Cipher.
##    The GUI will accept input from the user and output the desired phrase in
##    encrypted or decrypted format.
##
## Link to Wikipedia about the Vigenere Cipher :
##     http://en.wikipedia.org/wiki/Vigenère_cipher

# Import the graphics library.
from graphics import *
import time
    

# Define the encode function.

def code(encodeType, message, keyword):
    # Make the string uppercase to use the cipher
    message = message.replace(' ', '')
    messageUpper = message.upper()
    # Obtain the key (number of letters to shift in the alphabet)
    keyword = keyword.replace(' ', '')
    keyUpper = keyword.upper()
    # Creating two empty lists to append values to for message and keyword
    messageValues = []
    keywordValues = []
    # Creating more list(s) to store the code that will be returned
    codeValues = []
    finalEncode = []
    finalDecode = []
    # creating a counter for the key index position
    keyIndex = 0
    # Conditional to encode/decode/or return no value 
    if (encodeType == 'Encode') and len(message) > 0 and len(keyword) > 0:
        # Loop to access each letter in message and convert to ascii 
        for letter in messageUpper:
            encodeMessageNum = ((ord(letter) - 65))
            # Appending values to a master message number list
            messageValues.append(encodeMessageNum)
        # Another loop to access each letter in keyword and convert to ascii
        for letter in keyUpper:
            encodeKeyNum = ((ord(letter) - 65))
            # Appending values to a master keyword number list
            keywordValues.append(encodeKeyNum)
        # Loop through the message number list, and apply the formula to use the cipher
        for value in messageValues:
            code = (value + keywordValues[keyIndex]) % 26
            # Appending values to master encoded list, and advancing the key index count
            codeValues.append(code)
            keyIndex += 1
            # Conditional to loop through keyword in case we run out of letters
            if keyIndex == len(keywordValues):
                keyIndex = 0
        # Converting master encoded values to letters, and placing that in a list
        for value in codeValues:
            codeToLetter = chr(value + 65)
            finalEncode.append(codeToLetter)
        return finalEncode
    # Below code is almost exactly the same, but uses subtraction to decrypt a coded message
    elif (encodeType == 'Decode') and not len(message) == 0 and not len(keyword) == 0:
        for letter in messageUpper:
            decodeMessageNum = ((ord(letter) - 65))
            messageValues.append(decodeMessageNum)
        for letter in keyUpper:
            decodeKeyNum = ((ord(letter) - 65))
            keywordValues.append(decodeKeyNum)
        for num in messageValues:
            # Using absolute value of the difference, instead of addition
            code = abs((num - keywordValues[keyIndex]) % 26)
            codeValues.append(code)
            keyIndex += 1
            if keyIndex == len(keywordValues):
                keyIndex = 0
        for value in codeValues:
            codeToLetter = chr(value + 65)
            finalDecode.append(codeToLetter)
        return finalDecode
    elif len(message) == 0 or len(keyword) == 0:
        text = 'Nothing Entered in Phrase and/or Keyword'
        return text

# Creating a function to produce buttons.

def createButton(anchorPoint, textString):
    # Using parameters above, we will create a standard button.
    button = Rectangle((anchorPoint), (Point((anchorPoint.getX() + 80), (anchorPoint.getY() + 50))))
    # Cloning button to create a shadow effect
    buttonShadow = button.clone()
    # Setting button styles
    button.setOutline('white')
    button.setWidth(2)
    button.setFill(color_rgb(100, 149, 237))
    # Setting shadow styles
    buttonShadow.setFill('black')
    buttonShadow.move(3, 3)
    # Setting button text style
    buttonText = Text((button.getCenter()), (textString))
    buttonText.setTextColor('white')
    buttonText.setFace('helvetica')
    # return the various objects
    return button, buttonText, buttonShadow

# Create an animate button function.

def animateButton(button, buttonText):
    # moving the upper button to appear 'clicked'
    button.move(3, 3)
    buttonText.move(3, 3)
    # Changing the styles of the button when 'clicked'
    buttonText.setStyle('bold')
    button.setWidth(4)
    button.setFill(color_rgb(255, 99, 71))
    # Pause
    time.sleep(.5)
    # Undo the above changes, to make button appear to 'pop back out'
    button.move(-3, -3)
    buttonText.move(-3, -3)
    buttonText.setStyle('normal')
    button.setWidth(2)
    button.setFill(color_rgb(100, 149, 237))
    return

# Define a function to style the text on the window in a similar manner.

def setTextStyle(textObject, size, textColor, style):
    textObject.setFace('helvetica')
    textObject.setStyle(style)
    textObject.setSize(size)
    textShadow = textObject.clone()
    textShadow.move(2, 2)
    textObject.setTextColor(textColor)
    textShadow.setTextColor('black')
    return textObject, textShadow

# Define the main (GUI) function.

def main():

    # ---This section will create the GUI and all of its inputs and buttons.---
    # Create the window that will be presented to the user.
    win = GraphWin('Vignere Encoder / Decoder', 600, 400)

    # Making the window 'pop'
    win.setBackground('royal blue')

    # Create the title in the upper part of window
    titleText = Text(Point((win.getWidth() / 2), 40), 'Vigenere Cipher Encoder/Decoder')
    titleText, titleTextShadow = setTextStyle(titleText, 32, 'aquamarine', 'bold italic')
    titleTextShadow.draw(win)
    titleText.draw(win)

    # Create the first textual (phrase) entry object.
    phraseInput = Entry(Point(310, 100), 50)
    phraseInput.draw(win)
    phraseInput.setFace('courier')

    # Create the text to go next to the phrase entry box.
    phraseText = Text(Point(70, 100), 'Phrase :')
    phraseText, phraseShadow = setTextStyle(phraseText, 20, 'white', 'bold italic')
    phraseShadow.draw(win)
    phraseText.draw(win)

    # Create another textual (keyword) entry object.
    keywordInput = Entry(Point(240, 150), 30)
    keywordInput.draw(win)
    keywordInput.setFace('courier')

    # Create the text to go next to the keyword entry box.
    keywordText = Text(Point(70, 150), 'Keyword :')
    keywordText, keywordShadow = setTextStyle(keywordText, 20, 'white', 'bold italic')
    keywordShadow.draw(win)
    keywordText.draw(win)

    # Create the encode button.
    encodePoint1 = Point(150, 200)
    encodeButton, encodeText, encodeShadow = createButton((encodePoint1), 'Encode!')
    encodeShadow.draw(win)
    encodeButton.draw(win)
    encodeText.draw(win)

    # Create the decode button.
    decodePoint1 = Point(300, 200)
    decodeButton, decodeText, decodeShadow = createButton((decodePoint1), 'Decode!')
    decodeShadow.draw(win)
    decodeButton.draw(win)
    decodeText.draw(win)

    # Create an empty list to hold results
    resultingCode = []

    # Receive the input from the user clicking the mouse (coordinates)
    userClick = win.getMouse()

    # Initializing variables to hold the input form the entry boxes
    phrase = phraseInput.getText()
    keyword = keywordInput.getText()

    # Conditional to determine which button is being pressed, if any
    if userClick.getX() >= 150 and userClick.getX() <= 230 and userClick.getY() >= 200 and userClick.getY() <= 250:
        resultEncoded = code(('Encode'), phrase, keyword)
        animateButton((encodeButton), (encodeText))
        encodedString = ''.join(resultEncoded)
        resultingCode.append(encodedString)
    elif userClick.getX() >= 300 and userClick.getX() <= 380 and userClick.getY() >= 200 and userClick.getY() <= 250:
        resultDecoded = code(('Decode'), phrase, keyword)
        animateButton((decodeButton), (decodeText))
        decodedString = ''.join(resultDecoded)
        resultingCode.append(decodedString)
    else:
        noButtonString = 'No Button Was Clicked'
        resultingCode.append(noButtonString)
        
    print(resultingCode)

    # Remove the buttons from the display to make room
    encodeShadow.undraw()
    encodeButton.undraw()
    encodeText.undraw()
    decodeShadow.undraw()
    decodeButton.undraw()
    decodeText.undraw()

    # Create the text object that will display the code
    resultingMessage = Text((Point((win.getWidth() / 2), 200)), 'Resulting Message')
    codeTextObject = Text((Point((win.getWidth() / 2), 240)), resultingCode)

    # Using the setTextStyle() function to format the output
    resultingMessage, resultingShadow = setTextStyle(resultingMessage, 24, 'white', 'bold italic')
    codeTextObject, codeTextShadow = setTextStyle(codeTextObject, 24, 'tomato', 'bold')
    resultingShadow.draw(win)
    resultingMessage.draw(win)
    codeTextShadow.draw(win)
    codeTextObject.draw(win)

    # Create a button to allow another encryption.
    runAgainAnchor = Point(260, 280)
    runAgainButton, runAgainText, runAgainShadow = createButton((runAgainAnchor), 'Try Again?')
    runAgainShadow.draw(win)
    runAgainButton.draw(win)
    runAgainText.draw(win)

    # Create and display the click to close command
    clickToClose = Text((Point((win.getWidth() / 2), 375)), 'Click to Close')
    clickToClose, clickToCloseShadow = setTextStyle(clickToClose, 24, 'white', 'bold italic')
    clickToCloseShadow.draw(win)
    clickToClose.draw(win)

    # Close window by checking to see if user has clicked the button presented, or not
    userClick2 = win.getMouse()
    if userClick2.getX() >= 260 and userClick2.getX() <= 340 and userClick2.getY() >= 270 and userClick2.getY() <= 320:
        animateButton((runAgainButton), (runAgainText))
        win.close()
        main()
    else:
        win.close()
        print(userClick2.getX(), userClick2.getY())
    

# Call the main function.
main()
