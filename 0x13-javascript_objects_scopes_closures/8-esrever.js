#!/usr/bin/node
module.exports.esrever = function (list) {
  const tmplist = [];
  for (let i = list.length - 1; i >= 0; i--) {
    tmplist.push(list[i]);
  }
  return tmplist;
};
