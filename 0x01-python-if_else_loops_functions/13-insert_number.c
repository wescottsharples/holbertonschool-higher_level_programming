#include <stdlib.h>
#include "lists.h"

listint_t *insertion(listint_t *ptr, int number, int flag)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	if (flag)
		new->next = ptr;
	else
	{
		new->next = ptr->next;
		ptr->next = new;
	}

	return (new);
}

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *next;

	ptr = *head;

	if (!ptr)
		return (NULL);

	if (number < ptr->n)
		return (insertion(ptr, number, 1));

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
