#include <stdlib.h>
#include "lists.h"

/**
 * insertion - creates and inserts a node
 * @ptr: node to be inserted after
 * @number: number to be contained within new node
 * @flag: flag to signal if ptr is head of linked list
 *
 * Return: Address of newly created node on success, else NULL.
 */
listint_t *insertion(listint_t *ptr, int number, int flag)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	if (flag)
	{
		new->next = ptr;
	}
	else
	{
		new->next = ptr->next;
		ptr->next = new;
	}

	return (new);
}

/**
 * insert_node - finds position for a new node in an ordered linked list
 * @head: the start of the linked list
 * @number: number to be contained within new node
 *
 * Return: Address of newly created node on success, else NULL.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *next;

	if (!head || !*head)
		return (NULL);

	ptr = *head;

	if (number < ptr->n)
	{
		*head = (insertion(ptr, number, 1));
		return (*head);
	}

	while (ptr)
	{
		next = ptr->next;

		if (!next)
			return (insertion(ptr, number, 0));
		if (number < next->n)
			return (insertion(ptr, number, 0));

		ptr = next;
	}

	return (NULL);
}
