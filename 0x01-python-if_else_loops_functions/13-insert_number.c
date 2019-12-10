#include "lists.h"
/**
 * insert_node - insert node in a sorted linked list.
 * @head: linked list head address.
 * @number: number of new node to insert.
 * Return: address of the newly created node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *p, *np, *newadd;

	if (*head == NULL)
	{
		*head = malloc(sizeof(listint_t));
		(*head)->n = number;
		(*head)->next = NULL;
		return (*head);
	}
	p = *head;
	while (p != NULL)
	{
		if (p->n <= number && p->next->n > number)
		{
			np = p->next;
			p->next = malloc(sizeof(listint_t));
			newadd = p->next;
			p->next->n = number;
			p->next->next = np;
			break;
		}
		else
		{
			p = p->next;
		}
	}
	if (p == NULL)
	{
		np = p->next;
		p->next = malloc(sizeof(listint_t));
		newadd = p->next;
		p->next->n = number;
		p->next->next = np;
	}
	return (newadd);
}
