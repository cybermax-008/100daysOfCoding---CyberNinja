#include<bits/stdc++.h>

using namespace std;

class Node{
    public:
        int data;
    Node* next;
};

void print_list(Node* n){
    while(n != NULL){
        cout << n->data<< " ";
        n = n->next;
    }
    cout <<"\n";
}

int main(){
    // Create three nodes pointing to NULL initially
    Node* head = NULL;
    Node* first = NULL;
    Node* second = NULL;

    //allocate 3 nodes 
    head = new Node();
    first = new Node();
    second = new Node();

    //Store data and pointers
    head->data = 2;
    head->next = first;
    first->data = 3;
    first->next = second;
    second->data = 5;
    second->next = NULL;

    //printing the linkedlist
    print_list(head);

    return 0;
}
