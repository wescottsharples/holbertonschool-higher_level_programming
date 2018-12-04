#include "lists.h"

/**
 * check_cycle - function checks a linked list for a cycle
 * @list: pointer to first node in linked list
 * Return: 1 if cyclical, else 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *last, *new;

	if (!list)
		return (0);
	last = list;
	new = last->next;

	while (1)
	{
		if (!new)
			return (0);
		if (new == last)
			return (1);
		new = new->next;
		if (!new)
			return (0);
		new = new->next;
		if (!new)
			return (0);
		last = last->next;
	}

	return (0);
}
