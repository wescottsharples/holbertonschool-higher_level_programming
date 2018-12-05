#include <stdlib.h>
#include "lists.h"

listint_t *insertion(listint_t *ptr, int number)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = ptr->next;
	ptr->next = new;

	return (new);
}

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *next;
	int i;

	ptr = *head;

	if (!ptr)
		return (NULL);

	if (number < ptr->n)
		return (insertion(ptr, number));

	for (i = 0; ptr; i++)
	{
		next = ptr->next;

		if (!next)
			return (insertion(ptr, number));
		if (number < next->n)
			return (insertion(ptr, number));

		ptr = next;
	}

	return (NULL);
}
