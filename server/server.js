require("dotenv").config();
const express = require("express");
const cors = require("cors");
const path = require("path");

const connectDB = require("./config/db");

const authRoutes = require("./routes/authRoutes");
const itemRoutes = require("./routes/itemRoutes");
const adminRoutes = require("./routes/adminRoutes");
const claimRoutes = require("./routes/claimRoutes");

const app = express();

// Connect to MongoDB
connectDB();

// ===== Middleware =====
app.use(cors());
app.use(express.json());

// Make the "uploads" folder public so item images can be viewed in the browser
app.use("/uploads", express.static(path.join(__dirname, "uploads")));

// ===== API Routes =====
app.use("/api/auth", authRoutes);
app.use("/api/items", itemRoutes);
app.use("/api/admin", adminRoutes);
app.use("/api/claims", claimRoutes);

app.get("/api/health", (req, res) => {
    res.json({ message: "ReClaim server is running" });
});

app.get("/health", (req, res) => {
    res.json({
        status: "ok",
        commit: process.env.GIT_COMMIT_SHA || "unknown",
    });
});

// ===== Serve the built React frontend =====
const clientBuildPath = path.join(__dirname, "../client/dist");
app.use(express.static(clientBuildPath));

// Any non-API, non-upload route falls through to the React app (client-side routing)
app.get(/^\/(?!api|uploads).*/, (req, res) => {
    res.sendFile(path.join(clientBuildPath, "index.html"));
});

// ===== Error handler for file upload errors =====
app.use((error, req, res, next) => {
    if (error) {
        return res.status(400).json({ message: error.message });
    }
    next();
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`ReClaim server running on http://localhost:${PORT}`);
});