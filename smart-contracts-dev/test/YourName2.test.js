// test/Box.test.js
// Load dependencies
const { expect } = require('chai');

// Import utilities from Test Helpers
const { expectRevert } = require('@openzeppelin/test-helpers');

// Load compiled artifacts
const YourName = artifacts.require('YourName');

// Start test block
contract('YourName', function ([ owner, other ]) {

  // Use large integers ('big numbers')
  const value = new String('LSY');

  beforeEach(async function () {
    this.YourName = await YourName.new({ from: owner });
  });

  it('retrieve returns a value previously stored', async function () {
    await this.YourName.store(value, { from: owner });

    // Use large integer comparisons
    assert.isString(await this.YourName.retrieve(), value);
    // expect().to.be.String.equal(value);
  });

  
  it('non owner cannot store a value', async function () {
    // Test a transaction reverts
    await expectRevert(
      this.YourName.store(value, { from: other }),
      'Ownable: caller is not the owner'
    );
  }); 
});