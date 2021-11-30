@author JieGao
"""
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

var addTwoNumbers = function(l1, l2) {
    let temp = ((l1?l1.val:0)+(l2?l2.val:0));
        l1=(l1?l1.next:undefined);
        l2=(l2?l2.next:undefined);
    let plus = (temp>=10?1:0);
    let list = new ListNode(temp>=10?(temp-10):temp);
    let selectedNode = list;                              
    while(l1 || l2){
        temp = ((l1?l1.val:0)+(l2?l2.val:0)) + plus;
        l1=(l1?l1.next:undefined);
        l2=(l2?l2.next:undefined);
        plus = (temp>=10?1:0);
        selectedNode.next = new ListNode(temp>=10?(temp-10):temp);
        selectedNode = selectedNode.next;
    }
    if(plus>0){
        selectedNode.next = new ListNode(1);
        selectedNode = selectedNode.next;
    }
    return list;
    
};
