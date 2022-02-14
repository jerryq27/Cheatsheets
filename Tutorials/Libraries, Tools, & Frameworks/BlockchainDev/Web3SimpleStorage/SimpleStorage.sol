// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

/*
    Contracts can be thought of like a class.
*/
contract SimpleStorage {
    uint256 myNum; // In solidity, this will get initialized to a null value, in this case: 0.

    struct People {
        uint256 favoriteNumber;
        string name;
    }

    People[] public people;
    mapping(string => uint256) public nameToFavoriteNum;

    function store(uint256 _myNum) public {
        myNum = _myNum;
    }

    /*
        Two keywords that define functions:
        view - view functions read some state off of the blockchain. In Remix, functions that don't alter state create a blue buttons (public variables are also view functions!)
        pure - pure functions do some type of calculation, but pure functions also  don't alter the state.
    */
    function retrieve() public view returns (uint256) {
        return myNum;
    }

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        // Order matters when creating an object like this.
        // people.push(People(_favoriteNumber, _name));

        // Order doesn't matter when specifying the names.
        people.push(People({name: _name, favoriteNumber: _favoriteNumber}));

        nameToFavoriteNum[_name] = _favoriteNumber;
    }
}
