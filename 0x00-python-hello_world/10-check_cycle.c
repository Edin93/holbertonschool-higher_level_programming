#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: the head of the list to check.
 * Return: 0 if no cycle, 1 if there's one.
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp, *head;

	head = list;
	while (head != NULL)
	{
		tmp = head;
		while (head->next != NULL)
		{
			if (tmp == head->next)
				return (1);
			head = head->next;
		}
		head = head->next;
	}
	return (0);
}
