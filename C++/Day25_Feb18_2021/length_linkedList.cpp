#include<bits/stdc++.h>

using namespace std;

class Node{
    public:
        int data;
    Node* next;
};

void print_list(Node* n){
    if(n == NULL){
        cout << "The linked list is Empty!";
    }
    while(n != NULL){
        cout << n->data<< " ";
        n = n->next;
    }
    cout <<"\n";
}

void push(Node** head_ref, int num){
    Node* new_node = new Node();
    new_node->data = num;
    if(*head_ref == NULL){
        new_node->next = NULL;
        *head_ref = new_node;
        return;
    }
    new_node->next = *head_ref;
    *head_ref = new_node;

}

void insertAfter(Node* prev_node, int num){

    if (prev_node == NULL){
        return;
    }
    Node* new_node = new Node();

    new_node->data = num;
    new_node->next = prev_node->next;
    prev_node->next = new_node;
}

void append(Node** head_ref, int num){
    Node* new_node = new Node();
    new_node->data = num;
    new_node->next = NULL;
    if(*head_ref == NULL){
        *head_ref = new_node;
        return;
    }
    Node* curr_node = *head_ref;
    while(curr_node->next !=NULL){
        curr_node = curr_node->next;
    }
    curr_node->next = new_node;
    
}
void deleteFirstNode(Node** head_ref){
    if(!*head_ref){
        return;
    }
    Node* tempNode = *head_ref;
    *head_ref = (*head_ref)->next;
    delete tempNode;
}

void deleteLastNode(Node* head){
    if(!head){
        return;
    }
    if(head->next == NULL){
        return;
    }
    Node* second_last = head;
    while (second_last->next->next !=NULL){
        second_last =second_last->next;
    }
    delete second_last->next;
    second_last->next = NULL;
}

void deleteAfter(Node* pre_node){
    if(!pre_node){
        return;
    }
    Node* tempNode = pre_node->next;
    pre_node->next = pre_node->next->next;
    delete tempNode;
}

void deleteKey(Node** head_ref,int key){
    Node* curr_node = *head_ref;
    if(curr_node->data == key){
        *head_ref = (*head_ref)->next;
        delete curr_node;
        return;
    }
    while (curr_node->next->data != key)
    {
        curr_node = curr_node->next;
    }
    Node* temp_node = curr_node->next;
    curr_node->next = curr_node->next->next;
    delete temp_node;
    
}

void deletePos(Node** head_ref, int position){
    Node* curr_node = *head_ref;
    if(position == 0){
        *head_ref = (*head_ref)->next;
        delete curr_node;
        return;
    }
    int target_pos = 1;
    while(curr_node->next != NULL){
        if(target_pos==position){
            Node* temp_node = curr_node->next;
            curr_node->next = curr_node->next->next;
            delete temp_node;
            return;

        }
        curr_node = curr_node->next;
        target_pos++;

    }
}

void deleteLinkedList(Node** head_ref){
    Node* curr_node = *head_ref;
    if (!*head_ref){
        return;
    }
    while(curr_node->next != NULL){
        Node* temp_node = curr_node;
        curr_node = curr_node->next;
        delete curr_node;
    }
    *head_ref = NULL;
}

int length_iterative(Node* head){
    if(!head){
        return 0;
    }
    Node* curr_node = head;
    int count = 0;
    while(curr_node != NULL){
        curr_node = curr_node->next;
        count++;
    }
    return count;
}

int length_recursive(Node* head){
    if(!head){
        return 0;
    }
    else{
        return 1 + length_recursive(head->next);
    }
}

int main(){
    // Create a empty list
    Node* head = NULL;

    //Add few elements to the list 
    append(&head,2);
    append(&head,3);
    append(&head,5);
    append(&head,7);
    append(&head,10);
    append(&head,12);
    append(&head,15);

    //find the length of linked lsit
    int len_it= length_iterative(head);
    cout<<"Length using iteration:"<<len_it<<'\n';
    //using recursion
    int len_re = length_recursive(head);
    cout<<"Length using recursion:"<<len_re<<'\n';
    return 0;
}