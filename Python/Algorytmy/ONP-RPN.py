'''
Odwrotną notację polską ONP ( ang. RPN – Reverse Polish Notation ), zwana często również notacją Postfix, 
wymyślono w celu zapisywania dowolnych wyrażeń arytmetycznych bez nawiasów. 

W normalnym zapisie arytmetycznym operatory znajdują się pomiędzy argumentami: 
2 + 2     6 - 4     3 * 5     12 / 3

Operatory posiadają priorytety, czyli "ważność" oraz łączność w prawo lub w lewo. 
Jeśli w wyrażeniu wystąpią operatory o różnych priorytetach, to najpierw zostaną wykonane te ważniejsze:

3 + 5 * 2 = 3 + 10 = 13

Jeśli chcemy zmienić kolejność wykonywania działań, musimy używać nawiasów:

( 3 + 5 ) * 2 = 8 * 2 = 16

W ONP problem ten nie występuje. Operator zawsze występuje po swoich argumentach:

2 2 +     6 4 -     3 5 *     12 3 /

Dzięki tej prostej zasadzie nawiasy stają się zbędne:

3 + 5 * 2 → 3 5 2 * + = 3 10 + = 13
( 3 + 5 ) * 2 → 3 5 + 2 * = 8 2 * = 16

Source: https://eduinf.waw.pl/inf/alg/001_search/0102.php
'''
in progress
