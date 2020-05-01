#include "lists.h"
/**
 *insert_node - insert a number into a sorted
 *@head: pointer that point to the list
 *@number: number to add
 *Return: address of the added node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *old, *new, *current;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;
	old = NULL;
	current = *head;

	for (; current != NULL && current->n < number;)
	{
		old = current;
		current = current->next;
	}

	new->next = current;

	if (old != NULL)
		old->next = new;
	else
		*head = new;

	return (new);
}	
