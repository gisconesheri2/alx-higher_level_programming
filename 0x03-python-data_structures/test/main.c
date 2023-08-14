#include <stdio.h>
#include <stdlib.h>
#include <stdlib.h>

int main(void)
{
	int *list;
	int i = 0;

	list = malloc(sizeof(int) * 4);

	while (i < 4)
	{
		list[i] = i;
		i++;
	}

	printf("%d\n", list[0]);
	printf("%d\n", list[1]);
	printf("%d\n", list[2]);
	printf("%d\n", list[3]);

	return (0);
}
