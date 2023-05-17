objects = addition.o subtraction.o multiplication.o division.o main.o

calculator: $(objects) operations.h
	cc -o calculator $(objects)

$(objects): %.o:%.c
	cc -c $< -o $@

clean:
	rm -f $(objects)

