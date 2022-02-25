// SPDX-License-Identifier: MIT
pragma solidity >=0.5.0;

contract TodoList {
    // State variable that can be read (Solidity providers getters for public state variables).
    uint256 public taskCount = 0;

    struct Task {
        uint256 id;
        string content;
        bool completed;
    }
    mapping(uint256 => Task) public tasks;

    // Ran on deployment.
    constructor() public {
        createTask("Check out DappUniversity.com");
    }

    function createTask(string memory _content) public {
        taskCount++;
        tasks[taskCount] = Task(taskCount, _content, false);
    }
}
