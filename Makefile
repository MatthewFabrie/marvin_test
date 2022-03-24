##
## EPITECH PROJECT, 2022
## B-MAT-400-MPL-4-1-201yams-matthew.fabrie
## File description:
## Makefile
##

NAME	=	203hotline

all:
	cp $(NAME).py $(NAME)
	chmod +x $(NAME)

clean:
	rm -Rf __pycache__
	rm -Rf $(NAME)

fclean: clean re

test: clean re

re: clean re
