:- discontiguous parent/2.


% ----- 5 parent/2 facts -----
parent(abe, homer).
parent(mona, homer).
parent(clancy, marge).
parent(jacqueline, marge).
parent(herb, zeke).

% ----- 5 parents/3 facts -----
parents(homer, marge, bart).
parents(homer, marge, lisa).
parents(homer, marge, maggie).
parents(herb, clara, jill).
parents(bart, mary, jake).

% A person is a parent if they are one of the two in parents/3
parent(P, C) :- parents(P, _, C).   % P is the father
parent(P, C) :- parents(_, P, C).   % P is the mother

% A grandparent is a parent of a parent
grandparent(GP, GC) :-
    parent(GP, P),
    parent(P, GC).
