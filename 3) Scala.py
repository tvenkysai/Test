class KeyValueStore {
  // Internal storage for key-value pairs using a mutable Map
  private var store: Map[String, String] = Map()

  // Add or update a key-value pair in the store
  def put(key: String, value: String): Unit = {
    store = store + (key -> value)
  }

  // Retrieve the value associated with the key
  def get(key: String): Option[String] = {
    store.get(key)
  }

  // Remove the key-value pair from the store if it exists
  def remove(key: String): Unit = {
    store = store - key
  }

  // Return all keys currently in the store as a List
  def keys(): List[String] = {
    store.keys.toList
  }
}



// unit test process

import org.scalatest.funsuite.AnyFunSuite

class KeyValueStoreTest extends AnyFunSuite {
  test("put and get operations") {
    val store = new KeyValueStore
    store.put("name", "Alice")
    assert(store.get("name") == Some("Alice"))

    store.put("age", "30")
    assert(store.get("age") == Some("30"))
  }

  test("update existing key") {
    val store = new KeyValueStore
    store.put("name", "Alice")
    store.put("name", "Bob") // update the value
    assert(store.get("name") == Some("Bob"))
  }

  test("get non-existent key") {
    val store = new KeyValueStore
    assert(store.get("invalid") == None)
  }

  test("remove operation") {
    val store = new KeyValueStore
    store.put("name", "Alice")
    store.remove("name")
    assert(store.get("name") == None)
  }

  test("keys operation") {
    val store = new KeyValueStore
    store.put("name", "Alice")
    store.put("age", "30")
    assert(store.keys().sorted == List("age", "name").sorted)
  }

  test("remove non-existent key") {
    val store = new KeyValueStore
    store.put("name", "Alice")
    store.remove("invalid") // should not throw an error
    assert(store.keys() == List("name"))
  }
}



--Explanation Implementation How i Do:
put: Uses Map to store key-value pairs. If the key already exists, it updates the value.
get: Retrieves the value for a key wrapped in Option. If the key doesn't exist, it returns None.
remove: Deletes the key-value pair if the key exists.
keys: Returns all keys as a list.

--Explanation of Unit Tests:
put and get: Verifies basic put and get functionality.
update existing key: Ensures that updating a key works.
get non-existent key: Checks the behavior when fetching a non-existent key.
remove operation: Tests removal of an existing key.
keys operation: Ensures that all keys are returned correctly.
remove non-existent key: Ensures that trying to remove a non-existent key does not cause errors.
