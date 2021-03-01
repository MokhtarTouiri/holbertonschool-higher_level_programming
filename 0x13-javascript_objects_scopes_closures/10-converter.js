#!/usr/bin/node
module.exports.converter = function (base) {
  function operation (n) {
    return n.toString(base);
  }
  return operation;
};
