#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>
#include "lists.h"
/**
 * list_length - gets the number of nodes in a singly linked list
 * @head: pointer to the list
 * Return: number of nodes
 */
int list_length(listint_t **head)
{
	listint_t *current;
	int n;

	current = *head;
	n = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	return (n);
}
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the list
 * Return: 1 if the list is palindromic, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int *list_one, *list_two;
	int list_len, i, same;
	int linked_list_length = list_length(head);

	list_len = i = same = 0;
	if ((linked_list_length % 2) == 0)
		list_len = linked_list_length / 2;
	else
		list_len = (linked_list_length - 1) / 2;
	list_one = malloc(sizeof(int) * list_len);
	list_two = malloc(sizeof(int) * list_len);
	for (; i < list_len; i++)
	{
		*(list_one + i) = current->n;
		current = current->next;
	}
	if ((linked_list_length % 2) != 0)
		current = current->next;
	for (i = 0; i < list_len; i++)
	{
		*(list_two + i) = current->n;
		current = current->next;
	}
	for (list_len--, i = 0; list_len >= 0;)
	{
		if (list_one[i] == list_two[list_len])
		{
			same = 1;
			list_len--;
			i++;
			continue;
		}
		same = 0;
		break;
	}
	return (same);
}


