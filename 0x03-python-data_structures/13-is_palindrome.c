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
	listint_t *p1, *p2, *h = *head;
	int i, j, len, n1, n2;

	if (head == NULL || *head == NULL)
		return (1);

	len = calc_len(h);
	p1 = *head;
	for (i = 0; i < len / 2; i++)
	{
		n1 = p1->n;
		p2 = h;
		for (j = len / 2; j < len - 1 - i; j++)
		{
			p2 = p2->next;
		}
		n2 = p2->n;
		if (n1 != n2)
			return (0);
		p1 = p1->next;
	}

	return (1);
}
