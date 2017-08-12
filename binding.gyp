{
  "targets": [
    {
      "target_name": "<(module_name)",
      "type": "none",
      "sources": [ ],
      "actions": [
        {
          "action_name": "neon",
          "inputs": [],
          "outputs": ["../../native/index.node"],
          "conditions": [
            [
              "OS=='win'",
              { "action": ["neon build --path ../"] },
              { "action": ["neon", "build"] }
            ]
          ]
        }
      ],
    },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/../../native/<(module_name).node" ],
          "destination": "<(module_path)"
        }
      ]
    }
  ]
}
