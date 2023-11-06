#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to the head of listint_t
 * @n: integer to add in listint_t list
 * Return: address of the new element, or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *new_node;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);

    new_node->n = n;
    new_node->next = *head;
    *head = new_node;

    return (new_node);
}

/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @head: pointer to the head of listint_t
 * Return: 1 if it's a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *head_copy = *head;
    listint_t *aux = NULL, *aux_copy = NULL;

    if (*head == NULL || head_copy->next == NULL)
        return (1);

    while (head_copy != NULL)
    {
        add_nodeint(&aux, head_copy->n);
        head_copy = head_copy->next;
    }

    aux_copy = aux;
    while (*head != NULL)
    {
        if ((*head)->n != aux_copy->n)
        {
            free_listint(aux);
            return (0);
        }

        *head = (*head)->next;
        aux_copy = aux_copy->next;
    }

    free_listint(aux);
    return (1);
}
