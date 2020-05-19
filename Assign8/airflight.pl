flight(toronto,aircanada,london,500,360).
flight(london,aircanada,toronto,500,360).
flight(toronto,united,london,650,420).
flight(london,united,toronto,650,420).
flight(toronto,iberia,madrid,800,480).
flight(madrid,iberia,toronto,800,480).
flight(toronto,united,madrid,950,540).
flight(madrid,united,toronto,850,540).
flight(toronto,aircanada,madrid,900,480).
flight(madrid,aircanada,toronto,900,480).
flight(madrid,aircanada,barcelona,100,60).
flight(barcelona,aircanada,madrid,100,60).
flight(madrid,iberia,barcelona,120,65).
flight(barcelona,iberia,madrid,120,65).
flight(madrid,iberia,valencia,40,50).
flight(valencia,iberia,madrid,40,50).
flight(madrid,iberia,malega,50,60).
flight(malega,iberia,madrid,50,60).
flight(malega,iberia,valencia,80,120).
flight(valencia,iberia,malega,80,120).
flight(valencia,iberia,barcelona,110,75).
flight(barcelona,iberia,valencia,110,75).
flight(barcelona,iberia,london,220,240).
flight(london,iberia,barcelona,220,240).
flight(paris,united,toulouse,35,120).
flight(toulouse,united,paris,35,120).
airport(toronto,50,60).
airport(madrid,75,45).
airport(london,75,80).
airport(barcelona,40,30).
airport(malega,50,30).
airport(valencia,40,20).
airport(paris,50,60).
airport(toulouse,40,30).

check_flight(X,Y):-flight(X,A,Y,B,C).

check_cheap(A,B,C):-flight(A,C,B,X,Y), (X < 400).

check_two_flights(A,B):- flight(A,X,B,Y,Z), flight(A,P,B,Q,R), (X \= P).

check_cheap_ac(A,B,C):-flight(A,C,B,X,Y), (X < 400 ; C == aircanada).

check_same(A,B):-flight(A,X,B,Y,Z),flight(A,P,B,Q,R),(X==united , P==aircanada);(P==united , X==aircanada).