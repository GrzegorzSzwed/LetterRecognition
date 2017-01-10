# LetterRecognition
___________________________________________________
Oprogramowanie i narzędzia:
Python 3.4
OpenCV 3.2.0 - biblioteka do przetwarzania obrazów
NumPy 1.11.3 - biblioteka do obliczeń numerycznych, potrzebna do OpenCV
Keras 1.2.0 - biblioteka bazująca na Theano, służy do implementowania sieci neuronowej
Debian Jessie 8 - system operacyjny
PyCharm Community Edition - IDLE

****************************************************
Jak zaimportować?
Adres URL (github) github.com/GrzegorzSzwed/RozpoznawanieLiter.html
Szybkie importowanie projektu

otwórz terminal (command line- bash shell)
	$ git clone "adres URL"

lub
	kliknąć clone/download w Githubie i zaimportować do wybranej lokalizacji
___________________________________________________


Projekt : Systemy Wspomagające Podjemowanie Decyzji
Uczelnia: Politechnika Wrocławska
Data Oddania: 2017/01/...
Prowadzący :

Wykonali: 
Grzegorz Szwed 222315 @GrzegorzSzwed
Rafał Fojcik 218739

Wstęp:
Celem projektu jest znalezienie litery na obiekcie frezowanym i rozpoznanie jej w celu dobrania programu frezującego. 

Założenia:
A. Nie ma potrzeby analizowania obrazu z kamery. Rozpoznajemy litery z obrazu
B. Mamy za zadanie rozpoznać 5 liter od A do E.
C. Program ma nam mówić, na ile jest pewny swojej decyzji. (% zgodności)
