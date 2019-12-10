#include "lists.h"
/**
 * insert_node - insert node in a sorted linked list.
 * @head: linked list head address.
 * @number: number of new node to insert.
 * Return: address of the newly created node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *np, *newadd;

	if (*head == NULL)
	{
		*head = malloc(sizeof(listint_t));
		(*head)->n = number;
		(*head)->next = NULL;
		return (*head);
	}
	while (*head != NULL)
	{
		if ((*head)->n <= number && (*head)->next->n > number)
		{
			np = (*head)->next;
			(*head)->next = malloc(sizeof(listint_t));
			newadd = (*head)->next;
			(*head)->next->n = number;
			(*head)->next->next = np;
			break;
		}
		else
		{
			*head = (*head)->next;
		}
	}
	if (*head == NULL)
	{
		np = (*head)->next;
		(*head)->next = malloc(sizeof(listint_t));
		newadd = (*head)->next;
		(*head)->next->n = number;
		(*head)->next->next = np;
	}
	return (newadd);
}
