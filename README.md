Opis gry "Piano Game"
Dla gracza
„Piano Game” to gra rytmiczna, w której Twoim celem jest wciskanie odpowiednich klawiszy (D, F, J, K) w rytm muzyki. Nuty spadają w czterech ścieżkach, a Twoim zadaniem jest naciśnięcie odpowiedniego klawisza w momencie, gdy nuta dotrze do czerwonej linii u dołu ekranu.

Kluczowe elementy rozgrywki:

Trafienie w nutę w odpowiednim momencie przyznaje punkty.
Nietrafienie w nutę powoduje utratę zdrowia.
Gra kończy się, gdy Twoje zdrowie spadnie do zera.
Wskazówki:

Obserwuj czerwone linie na dole każdej ścieżki – to miejsce, w którym nuty muszą być trafione.
Wciśnięty klawisz zostaje podświetlony, aby ułatwić kontrolę nad akcją.
Dokładność i refleks są kluczowe, aby uzyskać wysoki wynik!


Dla programistów (opis techniczny)
Gra została napisana w Pythonie przy użyciu biblioteki Pygame. Kluczowe aspekty implementacji:

Mechanika gry:

Nuty są generowane dynamicznie na podstawie długości utworu oraz tempa (BPM).
Każda nuta jest instancją klasy Note, która zarządza jej pozycją i wizualizacją.
Trafienie nuty jest wykrywane, gdy znajduje się w obszarze docelowym (na wysokości czerwonej linii), a gracz wciśnie odpowiedni klawisz.
Wizualizacja:

Cztery ścieżki są rysowane w formie pionowych prostokątów.
Czerwone linie na dole ścieżek wskazują graczowi miejsce trafienia nut.
Wciśnięcie klawisza podświetla jego obszar na szary kolor, a trafienie nuty podświetla obszar docelowy na niebiesko.
Muzyka:

Utwór muzyczny jest odtwarzany za pomocą modułu pygame.mixer.music.
Czas trwania utworu jest wykorzystywany do synchronizacji generowania nut.
Obsługa punktacji i zdrowia:

Trafienie nuty dodaje punkty, a nietrafienie powoduje utratę zdrowia.
Stan gry (punkty, zdrowie) jest wyświetlany na ekranie.
Sterowanie:

Klawisze D, F, J, K odpowiadają czterem ścieżkom.
Parametry gry:

Tempo gry można dostosować, zmieniając zmienną NOTE_SPEED oraz wartość BPM w funkcji generate_notes.
Gra została zaprojektowana jako w pełni modyfikowalna i możliwa do rozbudowy – na przykład o nowe funkcje, poziomy trudności czy zaawansowaną synchronizację z rytmem muzyki.
