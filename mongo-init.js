// develompment only
db = db.getSiblingDB("helix");

db.createUser({
  user: "devuser",
  pwd: "123456",
  roles: [
    {
      role: "readWrite",
      db: "helix"
    }
  ]
});

db.createCollection("users");
