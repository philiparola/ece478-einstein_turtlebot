
"use strict";

let SetSpeed = require('./SetSpeed.js')
let StartController = require('./StartController.js')
let RestartController = require('./RestartController.js')
let SetCompliancePunch = require('./SetCompliancePunch.js')
let SetComplianceMargin = require('./SetComplianceMargin.js')
let TorqueEnable = require('./TorqueEnable.js')
let SetComplianceSlope = require('./SetComplianceSlope.js')
let SetTorqueLimit = require('./SetTorqueLimit.js')
let StopController = require('./StopController.js')

module.exports = {
  SetSpeed: SetSpeed,
  StartController: StartController,
  RestartController: RestartController,
  SetCompliancePunch: SetCompliancePunch,
  SetComplianceMargin: SetComplianceMargin,
  TorqueEnable: TorqueEnable,
  SetComplianceSlope: SetComplianceSlope,
  SetTorqueLimit: SetTorqueLimit,
  StopController: StopController,
};
