% ----- 10 facts -----
parent(homer, bart).
parent(homer, lisa).
parent(homer, maggie).
parent(marge, bart).
parent(marge, lisa).
parent(marge, maggie).
parent(abe,  homer).
parent(mona, homer).
parent(clancy, marge).
parent(jacqueline, marge).

% ----- 1 rule -----
grandparent(GP, GC) :-      % GP is grandparent of GC
    parent(GP, P),          % if GP is parent of P
    parent(P, GC).          % and P is parent of GC
