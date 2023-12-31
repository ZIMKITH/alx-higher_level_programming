#ifndef LISTS_H
#define LISTS_H

/* Std Lib */
#include <stdlib.h>

/* Struct */

/**
 * Struct listint_s - Linked lists WITH Structures
 * @n: Interger/ VALUE
 * @Next: Points to the next node
 *
 * Description: NODE structures for linked LIST
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/* Prototypes */
size_t print_listint(const listint_t *h);
int check_cycle(listint_t *list);
void free_listint(listint_t *head);
listint_t *add_nodeint(listint_t **head, const int n);

#endif
