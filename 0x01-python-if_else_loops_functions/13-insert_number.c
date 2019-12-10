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

	if (head == NULL)
		return (NULL);
	p = *head;
	if (p == NULL || p->n > number)
	{
		p = malloc(sizeof(listint_t));
		p->n = number;
		if (*head == NULL)
		{
			(*head)->next = NULL;
			return (p);
		}
		p->next = (*head);
		*head = p;
		return (p);
	}
	while (p->next != NULL)
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
		p = p->next;
	}
	if (p->n <= number && p->next == NULL)
	{
		np = p->next;
		p->next = malloc(sizeof(listint_t));
		newadd = p->next;
		p->next->n = number;
		p->next->next = NULL;
	}
	return (newadd);
}
