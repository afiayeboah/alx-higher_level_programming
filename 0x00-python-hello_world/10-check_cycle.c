#include "lists.h"

/**
* check_cycle - Checks if a linked list contains a cycle.
* @head: A pointer to the head of the linked list.
*
* Return: 1 if the list has a cycle, 0 if it doesn't.
*/
int check_cycle(listint_t *head)
{
	listint_t *slow_runner = head;
	listint_t *fast_runner = head;

	if (!head || !head->next)
	return (0);

	while (slow_runner && fast_runner && fast_runner->next)
	{
	slow_runner = slow_runner->next;
	fast_runner = fast_runner->next->next;

	if (slow_runner == fast_runner)
	return (1);
	}

	return (0);
}

