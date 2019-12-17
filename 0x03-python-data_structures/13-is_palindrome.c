#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * calc_len - calculate a linked list's length.
 * @head: address of the first list's node.
 * Return: length of the list.
 */
int calc_len(listint_t *head)
{
	int len = 0;

	while (head)
	{
		head = head->next;
		len++;
	}
	return (len);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: address of the list's head.
 * Return: 1 if it's a palindrome. 0 if it isn't.
 * An empty list is considered a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *p = *head;
	int i;
	int arr[2048];
	int len = calc_len(p);

	if (head == NULL || *head == NULL)
		return (1);

	i = 0;
	while (p)
	{
		arr[i] = p->n;
		p = p->next;
		i++;
	}

	for (i = 0; i < len; i++)
	{
		if (arr[i] != arr[len - 1 - i])
			return (0);
	}

	return (1);
}
