pragma solidity ^0.4.21;

contract Asset {
    address public issuer;
    mapping (address => uint) public balances;

    event Sent(address from, address to, uint amount);

    constructor() {
        issuer = msg.sender;
    }

    function issue(address receiver, uint amount) public {
        if (msg.sender != issuer) return;
        balances[receiver] += amount;
    }

    function send(address receiver, uint amount) public {
        if (balances[msg.sender] < amount) return;
        balances[msg.sender] -= amount;
        balances[receiver] += amount;
        emit Sent(msg.sender, receiver, amount);
    }
    
}
