from fastmcp import FastMCP

mcp = FastMCP("Google Drive Tools")



#tools 
@mcp.tool(description="Create Google Calender Events")
def create_event():
      pass





if __name__ == "__main__":
    mcp.run(transport='http', port=8000)